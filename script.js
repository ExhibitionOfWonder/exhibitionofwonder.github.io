VANTA.NET({
  el: "#animation-bg",
  mouseControls: true,
  touchControls: true,
  gyroControls: false,
  minHeight: 200.00,
  minWidth: 200.00,
  scale: 1.00,
  scaleMobile: 1.00,
  color: 0xff61,
  backgroundColor: 0x110b2f,
  points: 17.00
})

let n = 0;

function submitclicked() {
  n++
  let feedback = document.getElementById("feedback").value;
  let feedback_name = document.getElementById("feedback-name").value;
  console.log("Feedback #".concat(n, ": \"", feedback, "\" was sent by ", feedback_name))
  alert("Your feedback has been submitted!")
}