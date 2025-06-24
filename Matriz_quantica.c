typedef struct {
    unsigned short data : 14; // 14 bits por célula
    float phase;              // fase quântica
    float entropy;            // medida de entropia local
    int parity;               // bit de paridade quântica
} QubitCell;

QubitCell fractal_matrix[1000][1000];

void quantum_tick() {
    for (int i=0; i<1000; i++) {
        for (int j=0; j<1000; j++) {
            // exemplo de ajuste:
            fractal_matrix[i][j].phase += 0.01;
            fractal_matrix[i][j].entropy *= 0.99;
            // se entropia muito alta → fallback:
            if (fractal_matrix[i][j].entropy > 1.0) {
                fractal_matrix[i][j].data ^= 0x3FFF; // invert bits
                fractal_matrix[i][j].entropy = 0.5;  // reseta
            }
        }
    }
}
