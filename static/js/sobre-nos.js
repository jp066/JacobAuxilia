        function changeTab(selectedTab, sectionId) {
            // Remove the 'active' class from all tabs
            document.querySelectorAll('.tab').forEach(tab => {
                tab.classList.remove('active');
            });

            // Add the 'active' class to the clicked tab
            selectedTab.classList.add('active');

            // Hide all sections
            document.querySelectorAll('.mission-content').forEach(content => {
                content.classList.remove('active');
            });

            // Show the selected section
            document.getElementById(sectionId).classList.add('active');
        }