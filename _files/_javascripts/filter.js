filterSelection("all") // Execute the function and show all columns

function filterSelection(c) {
  var x, i;
  x = document.getElementsByClassName("column-feed-card");
  if (c == "all") {
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "";
    }
  }
  else {
    for (i = 0; i < x.length; i++) {
      categories = x[i].getAttribute('data-filter');
      if (filter_match(categories, c)) {
        x[i].style.display = "";
      }
      else {
        x[i].style.display = "none";
      }
    }
  }
}

function filter_match(categories, c) {
  // Some cards might not have the data-filter attribute.
  if (categories) {
    arr1 = categories.split(" ");
    for (i = 0; i < arr1.length; i++) {
      if(arr1[i] == c) {
        return true;
      }
    }
  }
  return false;
}

var btns = document.getElementsByClassName("cat-filter-js");
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function(){
    category = this.getAttribute('data-filter')
    filterSelection(category)
  });
}
