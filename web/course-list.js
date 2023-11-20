(function () {
    // your page initialization code here
    // the DOM will be available here
    console.log("DOM Initialized");
    getCourses();
})();


async function add() {
    var num1 = document.getElementById("num1").value;
    var num2 = document.getElementById("num2").value;

    const res = await fetch("http://127.0.0.1:8000/add/" + num1 + "/" + num2);
    var sum = await res.text();

    var result = document.getElementById("result");
    result.innerText = sum;
}

async function getCourses() {
    var res = await fetch("http://127.0.0.1:8000/courses");
    var courses = await res.json();

    var dropDownSelect = document.getElementById("course-list");
    for (var i = 0; i < courses.length; i++) {
        var option = document.createElement("option");
        option.text = courses[i]["name"];
        option.value = courses[i]["id"];
        dropDownSelect.add(option);
    }
}


