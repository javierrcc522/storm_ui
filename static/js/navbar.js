$(document).ready(function () {
    $("#sidebar").mCustomScrollbar({
         theme: "minimal"
    });
    $(document).ready(function () {
        $('#sidebarCollapse').on('click', function () {
            $('#sidebar').toggleClass('active');
            $('#sidebarCollapse').toggleClass('active');
        });
    });
});
