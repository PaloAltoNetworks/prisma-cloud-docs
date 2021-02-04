// Helpful resources:
// https://github.com/nakupanda/bootstrap3-dialog/
// https://nakupanda.github.io/bootstrap3-dialog/
// https://github.com/nakupanda/bootstrap3-dialog/issues/104
// https://community.algolia.com/algoliasearch-helper-js/gettingstarted.html
// https://community.algolia.com/algoliasearch-helper-js/reference.html

// Pressing Enter reloads page instead of submitting form:
// https://stackoverflow.com/questions/37450508/pressing-enter-reloads-page-instead-of-submitting-form

function twSearch() {

  var searchBtn = document.getElementById("tw-search-btn");
  var query = document.getElementById("tw-search-input");
  var form = document.getElementById("tw-search-form");
  var dialog;
  
  // Determine which search index to use.
  // window.location.pathname starts with "/". According to the split() reference:
  // If separator appears at the beginning (or end) of the string, it still has the effect of splitting.
  // The result is an empty (i.e. zero length) string, which appears at the first (or last) position of the returned array.
  // See: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/split
  // Debug
  //console.log(window.location.pathname)
  var alg_index = "twistlock_product";
  
  var pathArray = window.location.pathname.split('/', 3);
  
  if (pathArray.length == 3) {
    if (pathArray[2] == "staging") {
      alg_index = "staging";
    }
    else if (pathArray[2] == "compute_edition") {
      alg_index = "twistlock_product";
    }
    else if (pathArray[2] == "enterprise_edition") {
      alg_index = "enterprise_edition";
    }
    else if (pathArray[2] == "ops_guide") {
      alg_index = "ops_guide";
    }
    else if (pathArray[2] == "ref_arch") {
      alg_index = "ref_arch";
    }
    else if (pathArray[2] == "releases") {
      alg_index = "releases";
    }
  }

  // Initialize Algolia
  var client = algoliasearch('B706933OAL', 'bd17e0cd81f61dfe8b015ca5cf4915a6');
  
  var index = client.initIndex(alg_index);
  
  var helper = algoliasearchHelper(client, alg_index, {
    hitsPerPage:10
  });

  // Pressing enter in the input = search btn click
  form.addEventListener("submit", search, false)

  helper.on("result", searchCallback);


  // Pop open a dialog box, search the index, and display the results in the dialog.
  function search(event) {

    event.preventDefault();
 
    var queryString = query.value;
    //console.log(queryString);
    
    // Show the search result modal immediately.
    // The initial message says: Loading...
    dialog = new BootstrapDialog({
      type: BootstrapDialog.TYPE_DEFAULT,
      size: BootstrapDialog.SIZE_WIDE,
      title: 'Search results',
      message: $('<div class="model-search"><input id="search-input-dialog" type="text" /><button id="search-btn-dialog"><svg xmlns="http://www.w3.org/2000/svg" width="23" height="23" viewBox="0 0 29 29"><g fill="none" fill-rule="evenodd" stroke="#fff" stroke-linecap="square" stroke-linejoin="round" stroke-width="2" transform="rotate(-45 14.621 3.343)"><circle cx="7" cy="7" r="7"/><path d="M7 14L7 22"/></g></svg></button></div><div id="search-results">Loading...</div>'),
      onshown: function(dialogRef) {
        
        dialogRef.getModal().on('keyup', 'input#search-input-dialog', function(event) {
          event.preventDefault();
          if (event.keyCode == 13) {
            queryString = dialogRef.getModalBody().find('input').val();
            helper.setQuery(queryString).search();
          }
        });

        dialogRef.getModal().on('click', 'button#search-btn-dialog', function() {
          queryString = dialogRef.getModalBody().find('input').val();
          console.log("Query:", queryString);
          helper.setQuery(queryString).search();
        });

        // Populate the modal's input with the original search query, and set the focus on it.
        dialogInput = dialog.getModalBody().find('input');
        dialogInput.val(queryString);
        dialogRef.getModalBody().find('input').focus();
      }
    });
    
    //console.log(dialog);    
    dialog.realize();   
    dialog.open();
    
    // Query Algolia for the search results.
    helper.setQuery(queryString).search();
    
  }


  function searchCallback(content) {
   // Debug. Print all results returned from Algolia to the Javascript console.
   // console.log(content)
  
    var $searchResults = $('<div></div>');
  
    if (content.hits.length > 0) {
      // Format the search results into an HTML object.
      //   -Link to a page, where the link text is the sum of Article title + lvl1 heading + lvl2 heading + lvl3 heading.
      //   -Snippet of text from the page which includes the search term(s).
      for (var h in content.hits) {
        // Construct a link
        var linkText = null;
        // Article title
        if(content.hits[h]._highlightResult.hierarchy.lvl0)
          linkText = content.hits[h]._highlightResult.hierarchy.lvl0.value;
        // Append the H2 heading (if it exists in the result)
        if(content.hits[h]._highlightResult.hierarchy.lvl1)
          linkText += ' > ' + content.hits[h]._highlightResult.hierarchy.lvl1.value;
        // Append the H3 heading (if it exists in the result)
        if(content.hits[h]._highlightResult.hierarchy.lvl2)
          linkText += ' > ' + content.hits[h]._highlightResult.hierarchy.lvl2.value;
        // Append the H4 heading (if it exists in the result)
        if(content.hits[h]._highlightResult.hierarchy.lvl3)
          linkText += ' > ' + content.hits[h]._highlightResult.hierarchy.lvl3.value;

        var a = '<a href="';
        a += content.hits[h].url + '">';
        a += linkText + '</a>';

        // Append the link to the search results
        $searchResults.append(a);

        // Append a content preview, if it exists, to the search results.
        // Otherwise, append a blank line.
        var p = null;
        if (content.hits[h].content != null)
          p = '<p>' + content.hits[h]._highlightResult.content.value + '</p>';
        else
          p = '<p></p>';
        $searchResults.append(p);
      }
    }
    else {
      var p = '<p>' + "No results found." + '</p>';
      $searchResults.append(p);
    }
  
    // Overwrite the Loading message with the actual search results.
    dialog.getModalBody().find('div#search-results').html($searchResults);
  } 
}
