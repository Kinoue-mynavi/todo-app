import React from "react";
import { PageLayout } from "../../layout/PageLayout";
import { useFetchData } from "../../hooks/useFetchData";
import { Task } from "../../model/task";

type GetAllTasksResponse = {
    status: number;
    tasks: Task[];
}

const HomePage: React.FC = () => {
    const { data, isLoading, error } = useFetchData<GetAllTasksResponse>("/tasks");
    if (isLoading) return <p>Loading....</p>
    if (error) return <p>{JSON.stringify(error)}</p>

    return (
        <PageLayout>
            <table>
                <tr>
                    <th>ID</th>
                    <th>タイトル</th>
                    <th>概要・説明</th>
                    <th>ステータス</th>
                    <th>期限日</th>
                    <th>作成日</th>
                    <th>更新日</th>
                    <th>設定</th>
                </tr>
                {data?.tasks.map((task) => (
                    <tr key={task.id}>
                        <td>{task.id}</td>
                        <td>{task.title}</td>
                        <td>{task.description}</td>
                        <td>{task.status}</td>
                        <td>{task.deadline}</td>
                        <td>{task.created_at}</td>
                        <td>{task.updated_at}</td>
                        <td><a href="/">編集</a></td>
                    </tr>
                ))}
            </table>
        </PageLayout>
    );
};

export default HomePage;