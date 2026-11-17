import * as FileSystem from "expo-file-system/legacy";
import { useEffect, useState } from "react";
import { User } from "../schemas/User";

const FILE_URI =(FileSystem.documentDirectory ?? "") + "users.json";

export default function useUser() {
    const [users, setUsers] = useState<User[]>([]);

    //Chargement des utilisateurs
    useEffect(()=>{
        const loadUsers = async() => {
            console.log("Loading");
            try{
                const fileInfo = await FileSystem.getInfoAsync(FILE_URI);

                if (!fileInfo.exists) {
                    await FileSystem.writeAsStringAsync(FILE_URI, JSON.stringify([]));
                    setUsers([]);
                }
                else{
                    const content = await FileSystem.readAsStringAsync(FILE_URI);
                    setUsers(JSON.parse(content));
                }
            }
            catch(error){
                console.error("Erreur de chargements des utilisateurs");
                setUsers([]);
            }
        };
        loadUsers();
    }, []);

    const saveUsers = async(newUsers: User[]) => {
        try {
            console.log(newUsers);
            await FileSystem.writeAsStringAsync(FILE_URI, JSON.stringify(newUsers))
            setUsers(newUsers)
        } catch (error) {
            console.error("Erreur à la sauvegarde des utilisateurs : ", error);
        }
    };

    const addUser = (pseudo: string) =>
    {
        const newUser: User = {
            id:Date.now(),
            pseudo,
            dateInscription: new Date().toISOString()
        };
        console.log(JSON.stringify(newUser));
        saveUsers([...users, newUser]);
    };

    const deleteUser = (id:number) =>
    {
        console.log("delete", users.filter(u=>u.id==id), id);
        saveUsers(users.filter(u => u.id != id))
    }
    
    return {users, addUser, deleteUser};
}