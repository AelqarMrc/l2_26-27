import { Button, View, StyleSheet } from "react-native";
import { MyText } from "../compenents/MyText";
import useIdleGame from "../hooks/useIdleGame";
import { GlobalStyles as styles } from "../styles/global_styles";


export default function MainScreen()
{
  const {points, pointsPerSecond, upgradeCost, buyUpgrade} = useIdleGame();

  return (
    <View style={styles.container}>
      <MyText label="Points : " unit=' points' style={[styles.points]}>{points}</MyText>
      <MyText label='Points par seconde : ' unit=' points' style={[styles.pointsPerSecond]}>{pointsPerSecond}</MyText>
      <Button title={`UPGRADE - Coût : ${upgradeCost}`} onPress={buyUpgrade}></Button>
    </View>
  );
}