function openPopup() {
  document.getElementById("popup-container").style.display = "block";
}

function closePopup() {
  document.getElementById("popup-container").style.display = "none";
}

function openFilePopup(id, name, description, is_malicious) {
  document.getElementById("name").innerText = name;
  document.getElementById("file-description").innerText = description;
  document.getElementById("file-download").href = "/download/" + id;
  document.getElementById("malicious").innerText = is_malicious === "True" ? "" : "Not";
  document.getElementById("file-popup").style.display = "block";
}

function closeFilePopup() {
  document.getElementById("file-popup").style.display = "none";
}
