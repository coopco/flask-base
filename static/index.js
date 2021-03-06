window.onload = () => {
  $("#uploadbutton").click(() => {
    $("#progress").text("Processing...")
    link = $("#link");
    input = $("#fileinput")[0];
    if (input.files && input.files[0]) {
      let formData = new FormData();
      formData.append("file", input.files[0]);
      formData.append("plotseq", $("#plotseq").is(":checked"))
      $.ajax({
        url: "/",
        type: "POST",
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        error: function (data) {
          console.log("upload error", data);
          console.log(data.getAllResponseHeaders());
        },
        success: function (data) {
          update_progress(data);
        },
      });
    }
  });
};

// Code you want to run when processing is finished
async function update_progress(name) {
  $("#progress").text("")
  $("#link").css("visibility", "visible");
  $("#download").attr("href", "/uploads/" + name);
};


