function drawQuestion(que, i) {
  //question body
  let q = document.createElement("div");
  q.style.margin = "30px";

  //question
  let h = document.createElement("h4");
  h.innerHTML = i + 1 + ". " + que.question;

  //options
  let op = document.createElement("ul");
  for (let i = 0; i < que.options.length; i++) {
    let option = document.createElement("li");
    option.innerHTML = "<p>" + que.options[i] + "</p>";
    if (que.options[i][0] == que.answer) {
      option.style.color = "green";
      option.style.fontWeight = "bold";
    }

    op.appendChild(option);
  }

  q.appendChild(h);
  q.appendChild(op);
  document.body.appendChild(q);
}

function draw(data) {
  for (let i = 0; i < data.length; i++) {
    drawQuestion(data[i], i);
  }
}

function start() {
  axios
    .get("/data")
    .then(function (response) {
      draw(response.data);
    })
    .catch(function (error) {
      console.log(error);
    });
}

start();
