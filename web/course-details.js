async function fetchCourseDetails() {
    const response = await fetch("http://127.0.0.1:8000/courses-details/");

    if (response.ok) {
        const data = await response.json();

        data.forEach(course => {
            
            const courseCard = document.createElement("div");
            courseCard.className = "course-card";

          
            const courseLink = document.createElement("a");
            courseLink.href = course.url; 

    
            const courseImage = document.createElement("img");
            courseImage.src = course.imageSrc; 
            courseImage.alt = course.title;

            
            const courseTitle = document.createElement("h2");
            courseTitle.textContent = course.title;

            const courseDescription = document.createElement("p");
            courseDescription.textContent = course.description;

            
            courseLink.appendChild(courseImage);

            
            courseCard.appendChild(courseLink);
            courseCard.appendChild(courseTitle);
            courseCard.appendChild(courseDescription);

       
            document.querySelector(".dashboard").appendChild(courseCard);
        });
    }
    
    else 
    {
        console.error("Failed to fetch data");
    }
    
}

fetchCourseDetails();
