import numpy as np
import matplotlib.pyplot as plt
from typing import Optional
from dataclasses import dataclass

# Для начала тебе нужно объявить структуры данных, если их нет в заготовке:
@dataclass
class MatrixStatistics:
    matrix: np.ndarray
    row_means: np.ndarray
    col_means: np.ndarray
    row_vars: np.ndarray
    col_vars: np.ndarray

@dataclass
class TimeSeriesStatistics:
    mean: float
    variance: float
    std: float
    local_max_indices: np.ndarray
    local_min_indices: np.ndarray
    moving_average: np.ndarray


def sum_prod(matrices: list[np.ndarray], vectors: list[np.ndarray]) -> np.ndarray:
    # Складываем результаты перемножения каждой матрицы на её вектор
    result = np.zeros_like(vectors[0], dtype=np.float64)
    for A, x in zip(matrices, vectors):
        result += A @ x
    return result


def binarize(M: np.ndarray, threshold: float) -> np.ndarray:
    # Создаём копию, чтобы не менять исходную матрицу
    return (M > threshold).astype(int)


def unique_rows(M: np.ndarray) -> list[np.ndarray]:
    return [np.unique(row) for row in M]


def unique_columns(M: np.ndarray) -> list[np.ndarray]:
    return [np.unique(col) for col in M.T]


def matrix_statistics(m: int, n: int, mean: float, std: float, seed: Optional[int] = None) -> MatrixStatistics:
    rng = np.random.default_rng(seed)
    matrix = rng.normal(loc=mean, scale=std, size=(m, n))
    
    row_means = np.mean(matrix, axis=1)
    col_means = np.mean(matrix, axis=0)
    row_vars = np.var(matrix, axis=1)
    col_vars = np.var(matrix, axis=0)
    
    return MatrixStatistics(
        matrix=matrix,
        row_means=row_means,
        col_means=col_means,
        row_vars=row_vars,
        col_vars=col_vars
    )


def plot_histograms(stats: MatrixStatistics):
    # Вспомогательная функция для построения гистограмм
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    
    # Гистограмма средних по строкам
    axes[0].hist(stats.row_means, bins=10, alpha=0.7, label='Row Means')
    axes[0].set_title('Histogram of Row Means')
    axes[0].legend()
    
    # Гистограмма средних по столбцам
    axes[1].hist(stats.col_means, bins=10, alpha=0.7, label='Col Means', color='orange')
    axes[1].set_title('Histogram of Column Means')
    axes[1].legend()
    
    plt.tight_layout()
    plt.show()


def chess(m: int, n: int, a: int, b: int) -> np.ndarray:
    # Создаём матрицу индексов (i + j) % 2
    i, j = np.ogrid[:m, :n]
    mask = (i + j) % 2 == 0
    # Там где mask == True, ставим a, иначе b
    return np.where(mask, a, b)


def draw_rectangle(m: int, n: int, width: int, height: int, bg_color: tuple, rect_color: tuple) -> np.ndarray:
    img = np.full((m, n, 3), bg_color, dtype=np.uint8)
    
    x0, y0 = m // 2, n // 2
    # Вычисляем границы прямоугольника (учитываем, чтобы не выйти за края)
    x_start = max(0, x0 - height // 2)
    x_end = min(m, x0 + (height + 1) // 2)
    y_start = max(0, y0 - width // 2)
    y_end = min(n, y0 + (width + 1) // 2)
    
    img[x_start:x_end, y_start:y_end] = rect_color
    return img


def draw_ellipse(m: int, n: int, a: int, b: int, bg_color: tuple, ellipse_color: tuple) -> np.ndarray:
    img = np.full((m, n, 3), bg_color, dtype=np.uint8)
    
    x0, y0 = m // 2, n // 2
    
    # Создаём координатную сетку
    y, x = np.ogrid[:m, :n]
    
    # Уравнение эллипса (x - x0)^2 / a^2 + (y - y0)^2 / b^2 <= 1
    # Обрати внимание: в задаче x и y могут быть перепутаны в плане осей, 
    # но обычно x - это столбцы (n), y - строки (m).
    # Подставим: (x - y0)^2 / b^2 + (y - x0)^2 / a^2 <= 1, чтобы соблюсти размерности
    mask = ((x - y0) ** 2 / b ** 2) + ((y - x0) ** 2 / a ** 2) <= 1
    
    img[mask] = ellipse_color
    return img


def analyze_time_series(series: np.ndarray, p: int) -> TimeSeriesStatistics:
    mean = np.mean(series)
    variance = np.var(series)
    std = np.std(series)
    
    # Локальные максимумы и минимумы (исключая границы)
    local_max_indices = []
    local_min_indices = []
    
    for i in range(1, len(series) - 1):
        if series[i] > series[i - 1] and series[i] > series[i + 1]:
            local_max_indices.append(i)
        if series[i] < series[i - 1] and series[i] < series[i + 1]:
            local_min_indices.append(i)
            
    # Скользящее среднее
    if p > 0:
        moving_average = np.convolve(series, np.ones(p)/p, mode='valid')
    else:
        moving_average = np.array([])
        
    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        std=std,
        local_max_indices=np.array(local_max_indices),
        local_min_indices=np.array(local_min_indices),
        moving_average=moving_average
    )


def one_hot(labels: np.ndarray, class_count: Optional[int] = None) -> np.ndarray:
    if class_count is None:
        class_count = np.max(labels) + 1
        
    result = np.zeros((len(labels), class_count), dtype=int)
    
    # Используем продвинутую индексацию NumPy
    result[np.arange(len(labels)), labels] = 1
    return result