let net;

async function app() {
  console.log('Loading mobilenet..');

  // Load the model.
  net = await mobilenet.load();
  console.log('Sucessfully loaded model');

  // Make a prediction through the model on our image.
  const imgEl = document.getElementById('img');
  const result = await net.classify(imgEl);
  console.log(result);
  document.getElementById("predicted_text").innerHTML = "Classified image is - " + result[0].className;

}

function readURL(input) {
          if (input.files && input.files[0]) {
              var reader = new FileReader();

              reader.onload = function (e) {
                  $('#img')
                      .attr('src', e.target.result);
              };

              console.log(input.files[0])
              reader.readAsDataURL(input.files[0]);
          }
}

$("#file-picker").change(function () {
        readURL(this);
        app();
 });

