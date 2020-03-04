#include <iostream>
using namespace std;

float GetRemainingLogSpaceMegabyte() {
    FILE* pipe = popen("df -BM /var/log | tail -1 | awk '{print $4}' | cut -d'M' -f1", "r");
    if (!pipe) {
        return 1025;
    }

    char buffer[10] = {0};
    while(!feof(pipe)) {
        if(fgets(buffer, 10, pipe) != NULL) {
            break;
        }
    }
    pclose(pipe);

    return atof(buffer);
}

int main(void) {
	float mb = GetRemainingLogSpaceMegabyte();
	cout << "WTF: " << mb << endl;
	if (mb < 205350 && mb > 200000) {
		cout << "Fine" << endl;
	} else {
		cout << "NOO" << endl;
	}

	return 0;
}
