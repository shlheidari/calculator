

function num_editor(n) {
  let before = document.getElementById("p02").innerHTML
  document.getElementById("p02").innerHTML = (before*10)+n;
}

function op_editor(o) {
  let first_num = document.getElementById("p02").innerHTML
  document.getElementById("p02").innerHTML = 0;
  document.getElementById("first_num").value = first_num;
  document.getElementById("operator").value = o;
}

function sub() {
  let second_num = document.getElementById("p02").innerHTML
  document.getElementById("second_num").value = second_num;
  document.getElementById('form').submit();
}

function decimal() {
  let before = document.getElementById("p02").innerHTML
  document.getElementById("p02").innerHTML = before+'.';
}
