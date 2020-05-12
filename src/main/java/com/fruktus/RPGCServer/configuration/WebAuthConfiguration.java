package com.fruktus.RPGCServer.configuration;


import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.Ordered;
import org.springframework.core.annotation.Order;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;

@Configuration
@Order(Ordered.LOWEST_PRECEDENCE)
@EnableWebSecurity
@RequiredArgsConstructor
public class WebAuthConfiguration extends WebSecurityConfigurerAdapter {
    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http.authorizeRequests()
                .antMatchers("/register")
                .permitAll()
                .antMatchers("/v2/api-docs/**","/swagger.json","/swagger-ui.html","/swagger-resources/**","/webjars/**","/","/csrf")
                .permitAll()
                .anyRequest()
                .authenticated()
                .and()
                .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)
                .and()
                .httpBasic()
                .and()
                .csrf()
                .disable()
                .logout()
                .disable();
    }
}
