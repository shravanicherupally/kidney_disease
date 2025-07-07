document.addEventListener("DOMContentLoaded", () => {
  console.log("✅ JS Loaded");

  const form = document.querySelector("form");
  const inputs = form.querySelectorAll("input");

  form.addEventListener("submit", (e) => {
    let valid = true;
    inputs.forEach((input) => {
      const value = input.value.trim();
      if (value === "" || isNaN(value)) {
        valid = false;
        input.style.border = "2px solid red";
      } else {
        input.style.border = "1px solid #ccc";
      }
    });

    if (!valid) {
      e.preventDefault();
      alert("⚠️ Please enter valid numeric values.");
    }
  });
});
