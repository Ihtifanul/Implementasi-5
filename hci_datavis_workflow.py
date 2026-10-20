import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# 1. SIMULASI DATA PREPROCESSING UNTUK VISUALISASI
# Mensimulasikan data metrik kinerja atau analitik yang akan disajikan secara visual
# sesuai dengan prinsip kognitif dan data visualization yang efektif.

def prepare_visualization_data():
    print("[1/3] Menyiapkan Data untuk Visualisasi Antarmuka & Kinerja...")
    np.random.seed(42)
    
    # Kategori metrik atau waktu pengujian (misal: Hari 1 sampai 5)
    days = ['Hari 1', 'Hari 2', 'Hari 3', 'Hari 4', 'Hari 5']
    
    # Metrik performa sistem / tingkat keberhasilan tugas pengguna (%)
    task_success_rate = [72.5, 78.0, 85.2, 91.0, 95.8]
    error_rates = [15.2, 12.0, 8.5, 4.1, 1.5]
    
    df = pd.DataFrame({
        'Day': days,
        'Success_Rate': task_success_rate,
        'Error_Rate': error_rates
    })
    return df


# 2. EVALUASI USABILITY & METRIK KINERJA SISTEM (HCI Evaluation)
# Mensimulasikan evaluasi interaksi pengguna berdasarkan prinsip kepuasan & error.

def evaluate_usability_metrics(df):
    print("[2/3] Mengevaluasi Metrik Kebergunaan (Usability & Error Rate)...")
    
    avg_success = df['Success_Rate'].mean()
    final_error = df['Error_Rate'].iloc[-1]
    
    print("\n" + "="*50)
    print("      HASIL EVALUASI INTERAKSI MANUSIA KOMPUTER (IMK)")
    print("="*50)
    print(f"• Rata-rata Tingkat Keberhasilan (Success Rate) : {avg_success:.2f}%")
    print(f"• Penurunan Tingkat Kesalahan (Final Error)     : {final_error}%")
    
    if avg_success >= 85 and final_error <= 5:
        print("Status Evaluasi: INTERAKSI ANTARMUKA SANGAT INTUITIF & BAIK (Lulus Standard Usability)")
    else:
        print("Status Evaluasi: PERLU REDESAIN ANTARMUKA (High Cognitive Load)")
    print("="*50)


# 3. VISUALISASI DATA INTERAKTIF (Clean & Minimalist Chart)
# Menerapkan prinsip visualisasi data yang bersih tanpa chart junk (Edward Tufte).

def generate_clean_datavis_chart(df):
    print("[3/3] Membuat Grafik Visualisasi Data yang Bersih & Efektif...")
    
    fig, ax1 = plt.subplots(figsize=(8, 5))
    
    # Styling minimalis (Clean & No Chart Junk)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    
    # Plotting Success Rate
    color = '#2b5c8f'
    ax1.set_xlabel('Periode Pengujian', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Tingkat Keberhasilan (%)', color=color, fontsize=11, fontweight='bold')
    ax1.plot(df['Day'], df['Success_Rate'], color=color, marker='o', linewidth=2.5, label='Success Rate')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.set_ylim(50, 100)
    
    # Plotting Error Rate pada sumbu y kedua
    ax2 = ax1.twinx()
    color = '#d9534f'
    ax2.set_ylabel('Tingkat Kesalahan (%)', color=color, fontsize=11, fontweight='bold')
    ax2.plot(df['Day'], df['Error_Rate'], color=color, marker='s', linewidth=2.5, linestyle='--', label='Error Rate')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.set_ylim(0, 20)
    ax2.spines['top'].set_visible(False)
    
    plt.title('Dashboard Evaluasi Kinerja Sistem & Usability (HCI & DataVis)', fontsize=13, fontweight='bold', pad=15)
    fig.tight_layout()
    
    output_filename = "hci_datavis_performance.png"
    plt.savefig(output_filename, dpi=300)
    print(f"  -> Grafik visualisasi berhasil disimpan sebagai '{output_filename}'")
    plt.close()


# MAIN PROGRAM

if __name__ == "__main__":
    print("=== WORKFLOW: HUMAN-COMPUTER INTERACTION & DATA VISUALIZATION ===")
    
    # Step 1: Siapkan Data
    data_metrics = prepare_visualization_data()
    
    # Step 2: Evaluasi Metrik IMK
    evaluate_usability_metrics(data_metrics)
    
    # Step 3: Visualisasikan Data ke dalam Grafik Bersih
    generate_clean_datavis_chart(data_metrics)
    
    print("\n=== EKSEKUSI WORKFLOW SELESAI ===")