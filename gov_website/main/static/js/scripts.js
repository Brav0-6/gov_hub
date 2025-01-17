// Chatbot functionality placeholder
document.addEventListener('DOMContentLoaded', function () {
    const chatbotIcon = document.querySelector('.chatbot-icon');
    chatbotIcon.addEventListener('click', function () {
        alert('Chatbot is under construction!');
    });
});

// Scrolling news placeholder (infinite loop example)
const newsTicker = document.querySelector('.news-ticker');
if (newsTicker) {
    let offset = 0;
    setInterval(() => {
        offset -= 1;
        newsTicker.style.transform = `translateX(${offset}px)`;
        if (Math.abs(offset) >= newsTicker.scrollWidth) {
            offset = 0;
        }
    }, 30);
}
function toggleProfilePage() {
    var profilePage = document.getElementById("profilePage");
    if (profilePage.style.display === "none" || profilePage.style.display === "") {
        profilePage.style.display = "block";
    } else {
        profilePage.style.display = "none";
    }
}
document.addEventListener("DOMContentLoaded", () => {
    const profileIcon = document.getElementById("profile-icon");
    const dropdownMenu = document.getElementById("dropdown-menu");

    profileIcon.addEventListener("mouseenter", () => {
        dropdownMenu.style.display = "block";
    });

    profileIcon.addEventListener("mouseleave", () => {
        dropdownMenu.style.display = "none";
    });

    dropdownMenu.addEventListener("mouseleave", () => {
        dropdownMenu.style.display = "none";
    });

    dropdownMenu.addEventListener("mouseenter", () => {
        dropdownMenu.style.display = "block";
    });
});
document.addEventListener("DOMContentLoaded", function () {
    // Function to animate the counter
    function animateCountUp(element, target) {
        let start = 0;
        const duration = 2000; // 2 seconds
        const step = target / (duration / 16); // Approx. 16ms per frame

        function updateCounter() {
            start += step;
            if (start < target) {
                element.innerText = Math.floor(start).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                element.innerText = target.toLocaleString(); // Ensure final value
            }
        }

        updateCounter();
    }

    // Observer callback function
    function handleIntersection(entries, observer) {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                const element = entry.target;
                const targetValue = parseInt(element.getAttribute("data-target"), 10);
                animateCountUp(element, targetValue);
                observer.unobserve(element); // Stop observing after animation
            }
        });
    }

    // Create an observer instance
    const observer = new IntersectionObserver(handleIntersection, {
        threshold: 0.5, // Trigger when 50% of the section is visible
    });

    // Attach observer to each counter element
    document.querySelectorAll(".count").forEach((element) => {
        observer.observe(element);
    });
});
document.addEventListener("DOMContentLoaded", function () {
    const newsContainer = document.getElementById("news-container");

    fetch("https://newsapi.org/v2/everything?q=government&apiKey=YOUR_API_KEY")
        .then(response => response.json())
        .then(data => {
            data.articles.slice(0, 5).forEach(article => {
                const newsItem = document.createElement("div");
                newsItem.classList.add("news-item");
                newsItem.innerHTML = `
                    <h4><a href="${article.url}" target="_blank">${article.title}</a></h4>
                    <p>${article.description}</p>
                `;
                newsContainer.appendChild(newsItem);
            });
        })
        .catch(error => console.error("Error fetching news:", error));
});
