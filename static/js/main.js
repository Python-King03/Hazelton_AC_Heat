document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form[action='/contact']");

    form.addEventListener("submit", (e) => {
        // Honeypot check — bots die here
        const bot_field = form.querySelector("input[name='bot_field']");
        if (bot_field.value.trim() !== "") {
            e.preventDefault();
            return; // silently drop
        }

        // Grab fields
        const fname   = form.querySelector("input[name='fname']");
        const lname   = form.querySelector("input[name='lname']");
        const email   = form.querySelector("input[name='email']");
        const phone   = form.querySelector("input[name='phone']");
        const message = form.querySelector("textarea[name='message']");

        // Simple helpers
        const is_empty = (el) => el.value.trim() === "";

        const email_ok = (value) =>
            /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value);

        const phone_ok = (value) =>
            value === "" || /^[0-9()+\-\s]{7,}$/.test(value);

        let errors = [];

        if (is_empty(fname))   errors.push("First name is required.");
        if (is_empty(lname))   errors.push("Last name is required.");
        if (is_empty(email))   errors.push("Email is required.");
        if (!email_ok(email.value)) errors.push("Email format is invalid.");
        if (!phone_ok(phone.value)) errors.push("Phone number looks invalid.");
        if (is_empty(message)) errors.push("Message cannot be empty.");

        if (errors.length > 0) {
            e.preventDefault();
            alert(errors.join("\n"));
        }
    });
});

