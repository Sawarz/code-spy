package com.codespy.demo;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/test")
public class AnalyzerAPI {

    @GetMapping
    public String getAnalyze()
    {
        return "TEST TOMEK";
    }
}
