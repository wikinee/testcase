#include "helloworld.h"
#include <glibmm.h>
#include <glibmm/fileutils.h>
#include <giomm/file.h>
#include <iostream>
#include <fstream>

// add by niyl for finger login
#define LOGIN_PROTECT_LEVEL_PATH "/etc/userinfo/ProtectLevel"
#define LOGIN_USER_VERIFY_TYPE_PATH "/etc/userinfo/UserVerifyType"

HelloWorld::HelloWorld()
: m_button("Hello World")   // creates a new button with label "Hello World".
{
  // Sets the border width of the window.
  set_border_width(10);

  // When the button receives the "clicked" signal, it will call the
  // on_button_clicked() method defined below.
  m_button.signal_clicked().connect(sigc::mem_fun(*this,
              &HelloWorld::on_button_clicked));

  // This packs the button into the Window (a container).
  add(m_button);

  // The final step is to display this newly created widget...
  m_button.show();
}

HelloWorld::~HelloWorld()
{
}

void HelloWorld::on_button_clicked()
{
  std::cout << "check before\n" << std::endl;
  std::cout << "using finger login:" << getUsingFingerLogin() << std::endl;
  std::cout << "test atoi: " << std::atoi("ss") << std::endl;
  std::cout << "check after\n" << std::endl;
}

std::string HelloWorld::getFileFirstLine(const char *filename) {
  std::ifstream file(filename);
  std::string line;
  if (file.is_open()) {
    getline(file, line);
    file.close();
    return line;
  }
  return "";
}

int HelloWorld::getProtectLevle() {
  int i = 0;
  std::string first_line = getFileFirstLine(LOGIN_PROTECT_LEVEL_PATH);
  if (!first_line.empty()) {
    i = atoi(first_line.c_str());
  }
  printf("ProtectLevel: %d\n", i);
  return i;
}


int HelloWorld::getUserVerifyType() {
  int i = 0;
  std::string first_line = getFileFirstLine(LOGIN_USER_VERIFY_TYPE_PATH);
  if (!first_line.empty()) {
    i = atoi(first_line.c_str());
  }
  printf("UserVerifyType: %d\n", i);
  return i;
}

bool HelloWorld::getUsingFingerLogin() {
  if (getProtectLevle() + getUserVerifyType() == 0) {
    return false;
  }
  return true;
}