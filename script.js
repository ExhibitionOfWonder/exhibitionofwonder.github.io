
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
  points: 20.00
});

let n = 0;
let feedback_list = document.getElementById("feedback-list")
let sion_yoon_images = [
  "image/1.jpg", // 0
  "image/2.jpg", // 1
  "image/3.jpg", // 2
  "image/4.jpg", // 3
  "image/5.jpg" // 4
]

function submitclicked() {;
  n++;
  let feedback = document.getElementById("feedback").value;
  let feedback_name = document.getElementById("feedback-name").value;
  let complete_feedback = "Feedback #".concat(n, ": \"", feedback, "\" was sent by ", feedback_name)
  console.log(complete_feedback);
  feedback_list.innerHTML = feedback_list.innerHTML.concat("<br>", complete_feedback)

  alert("Your feedback has been submitted!");
};

let imgnum = 0

document.getElementById("sion-yoon").addEventListener("click", () =>{
  document.getElementById("sion-yoon").src = sion_yoon_images[imgnum]
  if (imgnum <= 4){
    imgnum++
  }
  else if (imgnum = 5)
    {
    imgnum = 0
  }
  console.log(imgnum)
})