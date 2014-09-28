

<script type="text/javascript">

    var final_transcript = '';
    var recognizing = false;

    var language = 'en-GB';  // change this to your language

    $(document).ready(function() {

        // check that your browser supports the API
        if (!('webkitSpeechRecognition' in window)) {
            alert("Your Browser does not support the Speech API");

        } else {

            // Create the recognition object and define four event handlers (onstart, onerror, onend, onresult)

            var recognition = new webkitSpeechRecognition();
            recognition.continuous = true;         // keep processing input until stopped
            recognition.interimResults = true;     // show interim results
            recognition.lang = language;           // specify the language

            recognition.onstart = function() {
                recognizing = true;
                $('#instructions').html('Listening...');
                $('#start_button').html('Transcribe');
            };

            recognition.onerror = function(event) {
                console.log("There was a recognition error...");
            };

            recognition.onend = function() {
                recognizing = false;
            };

            recognition.onresult = function(event) {
                var interim_transcript = '';

                // Assemble the transcript from the array of results
                for (var i = event.resultIndex; i < event.results.length; ++i) {
                    if (event.results[i].isFinal) {
                        final_transcript += event.results[i][0].transcript;
                    } else {
                        interim_transcript += event.results[i][0].transcript;
                    }
                }
                var first_letter = final_transcript.charAt(0);
                final_transcript =  first_letter + final_transcript.slice(1);
                console.log("interim:  " + interim_transcript);
                console.log("final:    " + final_transcript);
                // update the web page
                if(final_transcript.length > 0) {
                    $('#transcript').html(final_transcript);
                    $.post("/api/GetQuestion",
                        JSON.stringify({'data': final_transcript}),
                        function( data ) {
                            $('#answer').html(data);
                        })
                    //$.post("/api/StartRecording")
                }
            };


            $("#start_button").click(function(e) {
                e.preventDefault();

                if (recognizing) {
                    recognition.stop();
                    // myFunction('test');
                    $('#start_button').html('Click to Start Again');
                    recognizing = false;
                } else {
                    final_transcript = '';

                    // Request access to the User's microphone and Start recognizing voice input
                    recognition.start();

                    $('#instructions').html('Allow the browser to use your Microphone');
                    $('#start_button').html('waiting');
                    $('#transcript').html('&nbsp;');
                }
            }
            // function myFunction(string) {
            //     start_Recording(string)             // the function returns the product of p1 and p2
            // }
            );
        }
    });

</script>