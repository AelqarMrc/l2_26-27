import { useState, useEffect } from "react";
import AsyncStorage from "@react-native-async-storage/async-storage";

const GAME_DATA_KEY_STORAGE = "gameData";

export default function useIdleGame() {

    // useState :
    // const [state, setState] = useState(initValue)
    // state = getter, setState = setter, useState = valeur initiale
    const [points, setPoints] = useState(0);
    const [pointsPerSecond, setPointsPerSecond] = useState(1);
    const [upgradeCost, setUpgradeCost] = useState(10);

    // Gain automatique des points
    useEffect(() => {
        const interval = setInterval(() => {
            setPoints(prev => prev + pointsPerSecond);
        }, 1000);
        return () => clearInterval(interval);
    }, [pointsPerSecond]);

    // Achat d'une amélioration
    const buyUpgrade = () => {
        //Affichage en JSON
        console.log(JSON.stringify({ points, pointsPerSecond, upgradeCost }));

        if (points >= upgradeCost) {
            setPoints(prev => prev - upgradeCost);
            setPointsPerSecond(prev => prev + 1);
            setUpgradeCost(prev => Math.floor(prev * 1.5));
        }
        else {
            console.warn("Not enough points to buy upgrade");
        }
    };

    useEffect(()=>{
        loadData();
        return () =>
        {
            console.log("démontage");
            saveData();
        }
    }, []);

    // On save les données à chaque fois qu'une donnée change car l'écran n'est pas démonté lorsqu'on met en pause l'écran
    useEffect(()=>{
        saveData();
    }, [points, pointsPerSecond, upgradeCost]);

    const saveData = async () => {
        const myData = JSON.stringify({points, pointsPerSecond, upgradeCost});
        try{
            await AsyncStorage.setItem(GAME_DATA_KEY_STORAGE, myData);
            console.log("Sauvegardé avec Succés");            
        }
        catch(error){
            console.error("Sauvegarde échouée");
        }
    };

    const loadData = async () => {
        try {
            const data = await AsyncStorage.getItem(GAME_DATA_KEY_STORAGE);
            if (data) {
                const {points, pointsPerSecond, upgradeCost} = JSON.parse(data);
                setPoints(points);
                setPointsPerSecond(pointsPerSecond);
                setUpgradeCost(upgradeCost);
                console.log("Chargement réussi !");
            }    
        } 
        catch (error) {
            console.error("Erreur lors du chargement des données");
        }
    }

    return {
        points, 
        pointsPerSecond, 
        upgradeCost, 
        buyUpgrade
    };
}