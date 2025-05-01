<?php
    // Spécifie que le contenu est du JSON
    header('Content-Type: application/json');

    // Inclure la connexion à la base de données
    include_once 'db_connection.php';

    try {
        // Préparer et exécuter la requête SQL
        $sql = "SELECT OBJECTID, X, Y, haut_tot, haut_tronc, tronc_diam FROM Arbre";
        $stmt = $conn->prepare($sql);
        $stmt->execute();

        // Récupérer les résultats en tableau associatif
        $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // Renvoyer les résultats en JSON
        echo json_encode($result);
    } catch (PDOException $e) {
        // Renvoyer l'erreur en JSON
        echo json_encode(["error" => $e->getMessage()]);
    }
?>
