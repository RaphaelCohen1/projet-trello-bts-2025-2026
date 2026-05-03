$(document).ready(function () {
    // Initialisation du calendrier
    $('#calendar').fullCalendar({
        locale: 'fr',
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        selectable: true,
        select: function(start) {
            const selectedDateOnly = start.format('YYYY-MM-DD');
            const currentTime = moment().format('HH:mm');
            const fullDateTime = `${selectedDateOnly}T${currentTime}`;
            $('#appointment_date').val(fullDateTime);
            $('#selectedDateText').text('Date sélectionnée : ' + moment(fullDateTime).format('dddd DD MMMM YYYY, HH:mm'));
            $('#calendarContainer').fadeOut();
            $('#appointmentModal').fadeIn();
        }
    });

    $('#closeBtn').click(function() {
        $('#appointmentModal').fadeOut();
        $('#calendarContainer').fadeIn();
    });

    // Envoi des données vers la base avec AJAX
    $('#appointment-form').on('submit', function(e) {
        e.preventDefault();

        const professional = $('#professional').val();
        const name = $('#name').val();
        const email = $('#email').val();
        const appointmentDate = $('#appointment_date').val();

        $.ajax({
            url: 'process_appointement.php',
            type: 'POST',
            data: {
                professional: professional,
                name: name,
                email: email,
                appointment_date: appointmentDate,
                description: ''
            },
            success: function(response) {
                console.log("Réponse PHP :", response);

                // Afficher dans le calendrier
                $('#calendar').fullCalendar('renderEvent', {
                    title: `RDV avec ${professional}`,
                    start: appointmentDate,
                    color: '#f57c00'
                });

                // Ajouter dans la liste
                $('#appointmentsList').append(`
                    <li>
                        <strong>${professional}</strong> - ${name} (${email})<br>
                        <em>${moment(appointmentDate).format('dddd DD MMMM YYYY, HH:mm')}</em>
                    </li>
                `);

                $('#appointment-form')[0].reset();
                $('#appointmentModal').fadeOut();
                $('#calendarContainer').fadeIn();
            },
            error: function(xhr, status, error) {
                console.error("Erreur AJAX :", error);
                alert("Erreur lors de l'envoi des données.");
            }
        });
    });
});
