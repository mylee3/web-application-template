package com.example.personapi.repository;

import com.example.personapi.model.Person;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class LoadDatabase {
    private static final Logger log = LoggerFactory.getLogger(LoadDatabase.class);

    @Bean
    CommandLineRunner initDatabase(PersonRepository repository) {

        return args -> {
            log.info("Preloading " + repository.save(new Person("John", "Smith", "jsmith@yahoo.com")));
            log.info("Preloading " + repository.save(new Person("Mary", "Doe", "marydoe@gmail.com")));
        };
    }
}
