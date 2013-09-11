$(function(){
    $('input[type=text].mask').setMask();
    $('input[type=text].mask-reverse').click(function(e){
        // Modified version of:
        // http://stackoverflow.com/a/1675345/639465
        e.preventDefault();

        if (this.setSelectionRange)
        {
            // ... then use it
            // (Doesn't work in IE)

            // Double the length because Opera is inconsistent about whether a carriage return is one character or two. Sigh.
            var len = this.value.length * 2;
            this.setSelectionRange(len, len);
        }
        else
        {
            // ... otherwise replace the contents with itself
            // (Doesn't work in Google Chrome)
            this.value = this.value;
        }

        // Scroll to the bottom, in case we're in a tall textarea
        // (Necessary for Firefox and Google Chrome)
        this.scrollTop = 999999;
    });
});
