import { StyleSheet } from 'react-native';

export const GlobalStyles = StyleSheet.create({
  globalText: {
    fontSize: 20, //
    color: 'blue', //
  },
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
    marginTop: 20
  },
  points: {
    fontSize: 10,
    marginVertical: 10,
    color: 'red',
  },
  pointsPerSecond: {
    fontSize: 10,
    marginBottom: 20,
    color: 'red',
  },
  input: { 
    flex: 1, 
    borderWidth: 1, 
    borderColor: "#ccc", 
    marginRight: 10, 
    paddingHorizontal: 10 
  },
  inputRow: { 
    flexDirection: "row", 
    marginBottom: 20 
  },
  userRow: { 
    flexDirection: "row", 
    justifyContent: "space-between", 
    alignItems: "center", 
    marginBottom: 10 
  },
});