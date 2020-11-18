// gcc test-json.c -o testjson `pkg-config --libs --cflags json-glib-1.0`
#include<stdio.h>
#include<glib.h>
#include<json-glib/json-glib.h>

#define USING_UKEY_LOGIN "/tmp/TESTKEYFILE"

const gchar*
test_json_parse (const gchar* keyname) {
    GError *error = NULL;
    gchar *val;
    JsonParser *ukey_parser;
    gboolean load_res;
    JsonNode *root;
    JsonObject *root_obj;

    ukey_parser = json_parser_new ();
    load_res = json_parser_load_from_file (ukey_parser, USING_UKEY_LOGIN, &error);
    if (error) {
        g_print ("parseKeyFile: json parser load file error");
        g_error_free (error);
        return NULL;
    }

    root = json_parser_get_root (ukey_parser);
    if (root) {
        root_obj = json_node_get_object (root);
        if (root_obj) {
            JsonNode *account = json_object_get_member (root_obj, keyname);
            if (account) {
                val = (gchar *)json_node_get_string (account);
                return (const gchar *)val;
            }
        }
    }
    g_print ("parse key file success, val: %s", val);

    return NULL;
}

int main() {
    const gchar* test_key = "key";
    const gchar* test_value;
    test_value = test_json_parse (test_key);
    g_print ("file: %s, test res: %s\n", __FILE__, test_value);

    return 0;
}
