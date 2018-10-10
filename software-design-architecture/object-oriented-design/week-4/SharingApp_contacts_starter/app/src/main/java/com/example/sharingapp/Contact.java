package com.example.sharingapp;

import java.util.UUID;

public class Contact {

    private String username = null;
    private String email = null;
    private String id = null;


    public Contact(String username, String email, String id) {
        this.username = username;
        this.email = email;

        if(id == null) {
            this.setId();
        } else {
            this.updateId(id);
        }
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getId() {
        return id;
    }

    public void setId() {
        this.id = UUID.randomUUID().toString();
    }

    public void updateId(String id) {
        this.id = id;
    }

}
