#include <iostream>
#include <stdio.h>
#include <fstream>
#include <cstring>
#include <string.h>
#include <filesystem>
using namespace std;

size_t win = 0;
string input;
string flag;

void init(){
    setvbuf(stdout,0,2,0);
    setvbuf(stderr,0,2,0);
    setvbuf(stdin,0,2,0);
}

void readFlag(){
    ifstream file("flag");
    if (!file.is_open()) {
        std::cerr << "Can not open the file: flag" << std::endl;
        exit(0); 
    }
    getline(file, flag); 
    file.close();
}

int main(){
    char data[0x30];
    char randomStr[0x30];
    char s[0x30];
    char name[0x30];

    init();

    memset(data,0,0x30);
    memset(randomStr,0,0x30);
    memset(s,0,0x30);
    memset(name,0,0x30);
    readFlag();

    ifstream file("randomString"); 
    if (!file.is_open()) {
        std::cerr << "Can not open the file: randomString" << std::endl;
        return 1; 
    }
    
    size_t i = 0;
    while (i < 0x20 && file.get(randomStr[i])) { 
        i++;
    }
    randomStr[i] = '\x00';

    file.close();

    puts("Hello, CTFer.");
    puts("Please input the key of admin: ");
    fgets(s,0x30,stdin);
    snprintf(name,0x30,"/%s.key",s);
    filesystem::path filePath(name);

    if(!std::filesystem::exists(filePath)){
        puts("Sorry, you are not admin");
        return 0;
    }

    cout << "Let's play a game, guess what my sentence is. If you guess correctly, I'll give you the flag." << endl;

    while(true){
        memset(data,0,0x30);
        cout << "Please input your string" << endl;
        cin >> input;
        if(input.size() > 0x20){
            cout << "Your string is too long!" << endl;
        }else if(input.size() < 0x20){
            cout << "Your string is too short!" << endl;
        }
        data[snprintf(data,0x20,"%s",input.c_str())] = '\x00';
        printf("Your string: %s\n",&data);
        if(!memcmp(data, randomStr, 0x20)){
            win = 1;
            break;
        }else{
            string result;
            cout << "Sorry, this is no my sentence, do you want to try again?(y/n)" << endl;
            cin >> result;
            if(result == "y"){
                continue;
            }else{
                break;
            }
        }
    }

    if(win){
        cout <<"You win the game!!!" << endl;
        cout <<"Here is you flag: " << flag << endl;
    }

    return 0;
}