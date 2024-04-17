
    function openNav() {
        document.getElementById("mySidebar").style.width = "250px";
        document.getElementById("main").style.marginLeft = "250px";
    }
    function closeNav() {
        document.getElementById("mySidebar").style.width = "0";
        document.getElementById("main").style.marginLeft = "0";
    }
    function performSearch() {
        const searchTerm = document.querySelector('.search-input').value;
        // Implement your search logic here (e.g., redirect to search results page)
        console.log(`Searching for: ${searchTerm}`);
    }
    function openLoginPopup() {
        const overlay = document.getElementById('overlay');
        overlay.style.display = 'block';
    }
    // // Redirect to the login page
    // function redirectToLoginPage() {
    // location.href = "login.html";
    // }
    function redirectToLoginPage() {
        // Open a new window or tab with the login page
        window.open('login.html', '_blank', 'width=400,height=300');

    }
    function scrollLeft() {
        const container = document.querySelector('.box-container');
        container.scrollBy({
          left: -container.clientWidth,
          behavior: 'smooth'
        });
      }
      
      function scrollRight() {
        const container = document.querySelector('.box-container');
        container.scrollBy({
          left: container.clientWidth,
          behavior: 'smooth'
        });
      }