var addFriendButton = document.getElementById("add-friend-btn");

var friendCountElement = document.getElementById("friend-count");

var friendCount = Math.floor(Math.random() * 100);
friendCountElement.textContent = friendCount;

addFriendButton.addEventListener("click", function() {
  friendCount++;
  friendCountElement.textContent = friendCount;
  addFriendButton.disabled = true;
  addFriendButton.textContent = "Очікується підтвердження";
});

$(document).ready(function() {
  var friendCount = 0;

  $("#add-friend-btn").click(function() {
    friendCount++;
    $("#friend-count").text(friendCount);
  });
});
