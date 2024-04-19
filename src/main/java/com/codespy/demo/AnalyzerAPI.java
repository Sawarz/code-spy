package com.codespy.demo;
import java.io.*;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.Arrays;
import java.util.concurrent.TimeUnit;

@RestController
@RequestMapping("/mati")
public class AnalyzerAPI {

    @GetMapping
    public String getAnalyze() throws IOException, InterruptedException {
        String s = null;

        try {

            // run the Unix "ps -ef" command
            // using the Runtime exec method:
            Process p = Runtime.getRuntime().exec("python analyzer_v1.3.py");

            BufferedReader stdInput = new BufferedReader(new
                    InputStreamReader(p.getInputStream()));

            BufferedReader stdError = new BufferedReader(new
                    InputStreamReader(p.getErrorStream()));

            // read the output from the command
            System.out.println("Here is the standard output of the command:\n");
            Integer increment = 0;
            String[] output = new String[10];
            while ((s = stdInput.readLine()) != null) {
                output[increment] = s;
                increment++;
            }
            String outputAsString = Arrays.toString(output);
            return outputAsString;

        }
        catch (IOException e) {
            StringWriter sw = new StringWriter();
            e.printStackTrace(new PrintWriter(sw));
            String exceptionAsString = sw.toString();
            return exceptionAsString;

        }


    }
}
