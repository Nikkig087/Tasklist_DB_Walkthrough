document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // datepicker initialization
    let datepicker = document.querySelectorAll(".datepicker");
    //formating the date
    M.Datepicker.init(datepicker, {
        format: "dd mmmm, yyyy",
        //we want done to show select
        i18n: {done: "Select"}
    });

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);
});