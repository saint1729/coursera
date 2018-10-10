package com.example.sharingapp;

import android.content.Context;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.lang.reflect.Type;
import java.util.ArrayList;

public class ContactList {

    private static ArrayList<Contact> contacts = null;
    private String FILENAME = "contacts.sav";

    public ContactList() {
        this.contacts = new ArrayList<>();
    }

    public ArrayList<Contact> getContacts() {
        return contacts;
    }

    public void setContacts(ArrayList<Contact> contacts) {
        this.contacts = contacts;
    }

    public ArrayList<String> getAllUsernames() {

        ArrayList<String> l = new ArrayList<>();

        if(contacts == null) {
            return l;
        }

        for(Contact c:this.contacts) {
            l.add(c.getUsername());
        }

        return l;
    }

    public void addContact(Contact contact) {
        contacts.add(contact);
    }

    public void deleteContact(Contact contact) {
        contacts.remove(contact);
    }

    public Contact getContact(int index) {
        return this.contacts.get(index);
    }

    public int getSize() {
        return this.contacts.size();
    }

    public int getIndex(Contact contact) {

        for(int i = 0; i < contacts.size(); i++) {
            if(contacts.get(i).getId().equals(contact.getId())) {
                return i;
            }
        }

        return -1;
    }

    public boolean hasContact(Contact contact) {
        return this.getIndex(contact) != -1;
    }

    public Contact getContactByUsername(String username) {
        for(Contact contact:this.contacts) {
            if(contact.getUsername().equals(username)) {
                return contact;
            }
        }
        return null;
    }

    public void loadContacts(Context context) {
        try {
            FileInputStream fis = context.openFileInput(FILENAME);
            InputStreamReader isr = new InputStreamReader(fis);
            Gson gson = new Gson();
            Type listType = new TypeToken<ArrayList<Contact>>() {}.getType();
            this.contacts = gson.fromJson(isr, listType);
            fis.close();
        } catch (FileNotFoundException e) {
            this.contacts = new ArrayList<Contact>();
        } catch (IOException e) {
            this.contacts = new ArrayList<Contact>();
        }
    }

    public void saveContacts(Context context) {
        try {
            FileOutputStream fos = context.openFileOutput(FILENAME, 0);
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            Gson gson = new Gson();
            gson.toJson(this.contacts, osw);
            osw.flush();
            fos.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public boolean isUsernameAvailable(String username) {
        return this.getContactByUsername(username) == null;
    }

}
