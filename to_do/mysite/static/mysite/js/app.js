
//     var popup1 = document.getElementById("popup-1")
// var openPopup1 = document.getElementById("open-popup-1")
// var closePopup1 = document.getElementById('close-popup-1')

// openPopup1.addEventListener('click', () => {
// 	popup1.style.display = "block";
// })

// closePopup1.addEventListener('click', () => {
// 	popup1.style.display = "none";
// })

// var myModal = document.getElementById('exampleModal')
// var myInput = document.getElementById('myInput')

// myModal.addEventListener('shown.bs.modal', function () {
//   myInput.focus()
//   //myModal.show()
// })

$(document).ready(function() {
    $("#myModal").modal();
  });


  $(document).on('click', '.like-button', function (e) {
    e.preventDefault();
    let post_id = $(this).val();
    $.ajax({
      type: 'POST',
      url: '{% url "posts:like" %}',
      data: {
        postid: post_id,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        action: 'post'
      },
      success: function (json) {
        // document.getElementById("like_count").innerHTML = json['result']
        $("#like_count" + post_id).html(json['result']);
      },
      error: function (xhr, errmsg, err) {
      }
    });
  })