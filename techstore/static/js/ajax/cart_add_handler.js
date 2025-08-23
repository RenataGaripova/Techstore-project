document.addEventListener("click", function(e) {
    const csrftokenElem = document.querySelector('[name=csrfmiddlewaretoken]');
    if (!csrftokenElem) return;
    const csrftoken = csrftokenElem.value;


    if (e.target.classList.contains("add-to-cart")) {
        const form = e.target.closest(".cart-form");
        const url = form.dataset.url;
        const quantity = form.querySelector("[name=quantity]").value;
    
        fetch(url, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrftoken,
                "X-Requested-With": "XMLHttpRequest",
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ quantity: quantity })
        })
        .then(res => res.json())
        .then(data => {
            console.log("Ответ корзины:", data);
            alert("✅ " + data.message);
        })
        .catch(err => console.error("Ошибка:", err));
    }


    if (e.target.classList.contains("add-to-wishlist")) {
        alert("💚 Wishlist пока не реализован, но кнопка работает!");
    }
});
