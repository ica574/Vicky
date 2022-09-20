function handleResponse(ans) {
  document.getElementById("answer").textContent = ans;
}
eel.expose(handleResponse);

function handleInput(input) {
  document.getElementById("input").textContent = input;
}
eel.expose(handleInput);

function handleLoaded(isLoaded) {
  if (isLoaded === true) {
    document.getElementById("answer").textContent =
      "Say Vicky to initialize...";
  } else {
    document.getElementById("answer").textContent = "Loading..";
  }
}
eel.expose(handleLoaded);
