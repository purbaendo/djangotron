function updateIframe(){
  var myFrame = $("#myframe").contents().find('body');
  var textareaValue = $("textarea").val();
  myFrame.html(textareaValue);
}