
function rand() {
    rn = Math.floor(Math.random() * 100);
    console.log(rn)
    min = 1
    max = 100
    i = 0
}

function myFunction() {
    i = ++i
    x = document.getElementById("number").value;
    document.getElementById("number").value = "";
    if (x == rn) {
        Swal.fire({
            title: "You Win",
            text: rn + " is correct number "+i+" round",
            icon: "success"
        }).then((result) => {
            if (result.isConfirmed) {
                location.reload()
            }
        })
    } else if (x > rn) {
        max = + x - 1
        Swal.fire({
            title: "Less Than",
            text: "The number is between " + min + " and " + max,
            icon: "error"
        });
    } else if (x < rn) {
        min = + x + 1
        Swal.fire({
            title: "Great Than",
            text: "The number is between " + min + " and " + max,
            icon: "error"
        });
    }
}
