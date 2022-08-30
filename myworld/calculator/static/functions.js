

function num_editor(n) {
  let before = document.getElementById("p02").innerHTML
  n_str = n.toString();
  if (before == 0) {
    document.getElementById("p02").innerHTML = n;
  } else {
    document.getElementById("p02").innerHTML = before + n_str
  }

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
