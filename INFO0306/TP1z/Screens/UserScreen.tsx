import { useState } from "react";
import { View, Text, TextInput, Button, FlatList } from "react-native";
import useUserFile from "../hooks/useUser";
import { User } from "../schemas/User";
import { GlobalStyles as styles } from "../styles/global_styles";

export default function UserScreen() {
    const { users, addUser, deleteUser } = useUserFile();
    const [pseudo, setPseudo] = useState("");

    return (
        <View style={styles.container}>
            <Text style={styles.title}>Utilisateurs</Text>

            <View style={styles.inputRow}>
                <TextInput
                    style={styles.input}
                    placeholder="Pseudo"
                    value={pseudo}
                    onChangeText={setPseudo} />
                <Button title="Ajouter" onPress={()=> {
                    if (pseudo) {
                        addUser(pseudo)
                        setPseudo("");
                    }
                }}/>
            </View>
            <FlatList
                data={users}
                keyExtractor={(item:User) => item.id.toString()}
                renderItem={({item})=> (
                    <View>
                        <Text>{item.pseudo}({new Date(item.dateInscription).toLocaleDateString()})</Text>
                        <Button title="Supprimer" onPress={() => deleteUser(item.id)}/>
                    </View>
                )}
            />
        </View>
    );
}