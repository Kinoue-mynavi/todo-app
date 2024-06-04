type StrDate = `${number}-${number}-${number}`;

export type Task = {
    id: number;
    title: string;
    status: string;
    description?: string;
    deadline?: StrDate;
    created_at: StrDate;
    updated_at: StrDate;
};
