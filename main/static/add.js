function first()
        {
            document.getElementById("firstform").style.display="none";
            document.getElementById("secondform").style.display="block";
            document.getElementById("signupbtn").style.borderBottom="2px solid #9E7676";
            document.getElementById("loginbtn").style.borderBottom="none";
        }

        function second()
        {
            document.getElementById("secondform").style.display="none";
            document.getElementById("firstform").style.display="block";
            document.getElementById("loginbtn").style.borderBottom="2px solid #9E7676";
            document.getElementById("signupbtn").style.borderBottom="none";
        }