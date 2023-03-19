<script>
    let className;
    export { className as class };
</script>

<div class="a {className}">習</div>
<slot />

<style lang="postcss" module>
    .a {
        @apply inline-flex items-center justify-center transition duration-200 ease-in-out h-6 leading-6 px-2.5
        border rounded-badge border-info border-opacity-50 bg-transparent text-info;
        width: fit-content;
    }
</style>
