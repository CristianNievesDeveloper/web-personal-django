//nav
        // Obtener elementos del DOM
        const hamburger = document.querySelector('.hamburger');
        const navBar = document.querySelector('.nav-bar');

        // Agregar evento al hacer clic en la hamburguesa
        hamburger.addEventListener('click', () => {
            // Alternar clase 'open' para mostrar/ocultar el menú
            navBar.classList.toggle('active');
        });

        // Agregar eventos a los enlaces del menú
        const navLinks = document.querySelectorAll('.nav-bar a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                // Remover clase 'open' para ocultar el menú después de hacer clic en un enlace
                navBar.classList.remove('active');
            });
        });

      //-------------------- Animacion Scrool
      const seccionesOcultas = document.querySelectorAll('.mob');

      const observer = new IntersectionObserver((entries)=>{
          entries.forEach((entry)=>{
              entry.target.classList.toggle('mostrar', entry.isIntersecting);
          })
      })
      seccionesOcultas.forEach((seccion)=>observer.observe(seccion)); 