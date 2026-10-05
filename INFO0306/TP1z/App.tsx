import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button } from 'react-native';
import { useState, useEffect } from 'react';

export default function App() {
  const [points, setPoints] = useState(0);
  const [pps, setPps] = useState(1);
  const [cost, setCost] = useState(10); // Initialisation du coût de l'amélioration

  useEffect(() => {
    const interval = setInterval(() => {
      setPoints(prev => prev + pps);
    }, 1000);

    // Correction: On retourne bien une fonction pour le nettoyage
    return () => clearInterval(interval);
  }, [pps]); // Se relance uniquement si le PPS change

  const handleUpgrade = () => {
    if (points >= cost) {
      setPoints(prev => prev - cost);
      setPps(prev => prev + 2); // Augmente de 2 par seconde comme sur la capture
      setCost(prev => Math.floor(prev * 1.5)); // Augmente le coût pour le prochain achat
      console.log(`Amélioration réussie ! Nouveau PPS : ${pps + 2}`);
    } else {
      console.error(`Erreur : Fonds insuffisants. Il manque ${cost - points} points.`);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Points: {points}</Text>
      <Text style={styles.text}>Points / sec: {pps}</Text>
      
      <View style={styles.buttonContainer}>
        <Button 
          title={`UPGRADE (+2 / SEC) - COÛT : ${cost}`} 
          onPress={handleUpgrade} 
        />
      </View>
      
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  text: {
    fontSize: 18,
    marginVertical: 5,
  },
  buttonContainer: {
    marginTop: 20,
  }
});