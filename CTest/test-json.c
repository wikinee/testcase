// gcc test-json.c -o testjson `pkg-config --libs --cflags json-glib-1.0`
#include<stdio.h>
#include<glib.h>
#include<json-glib/json-glib.h>


#define USING_UKEY_LOGIN "/tmp/TESTKEYFILE"

int main() {
    GError *error = NULL;
    const gchar *val;
    gchar *keyname = "key";
    JsonParser *ukey_parser = json_parser_new ();
    gboolean load_res = json_parser_load_from_file (ukey_parser, USING_UKEY_LOGIN, &error);
    if (error) {
        g_print ("parseKeyFile: json parser load file error");
        g_error_free (error);
        return 1;
    }

    JsonNode *root = json_parser_get_root (ukey_parser);

    if (root) {
        JsonObject *root_obj = json_node_get_object (root);
        if (root_obj) {
            JsonNode *account = json_object_get_member (root_obj, keyname);
            if (account) {
                val = json_node_get_string (account);
            }
        }
    }
    g_print ("parse key file success, val: %s", val);

    return 2;
}
